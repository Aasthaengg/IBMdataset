from math import gcd
import time

#pri_arr[i]におけるiの素因数のうち最大の数を持つ配列をつくる
#pri_arrはこんな感じになる↓
#[0, 0, 2, 3, 2, 5, 3, 7, 2, 3,...]
def make_prime_arr(max_a):
    pri_arr = [0] * max_a
    #start_time = time.time()
    for i in range(2, max_a):
        if(pri_arr[i] != 0):
            continue
        for j in range (i, max_a, i):
            pri_arr[j] = i
    #end_time = time.time()
    #print(end_time - start_time)
    return pri_arr


#pairwiseかどうかを判定する関数
def is_pairwise(a_arr, pri_arr, max_a):
    flg_arr = [0] * (max_a)
    for a_ele in a_arr:
        x = a_ele
        y = 0
        while x != 1:
            if(pri_arr[y] != pri_arr[x]):
                flg_arr[pri_arr[x]] += 1
            if flg_arr[pri_arr[x]] > 1:
                return False
            y = x
            x = x // pri_arr[x]
            
    return True


#setwiseかどうかを判定する関数
def is_setwise(a_arr, N):
    entire_gcd = a_arr[0]
    for i in range(1, N):
        entire_gcd = gcd(entire_gcd, a_arr[i])
    if entire_gcd != 1:
        return False        
    return True


def main():
    N = int(input())
    a_arr = list(map(int, input().split(" ")))
    max_a = 10**6 + 1
    pri_arr = make_prime_arr(max_a)
    if is_pairwise(a_arr, pri_arr, max_a):
        print("pairwise coprime")
    elif is_setwise(a_arr, N):
        print("setwise coprime")
    else:
        print("not coprime")

if __name__ == "__main__":
    main()