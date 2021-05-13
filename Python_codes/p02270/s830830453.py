from sys import stdin

def solve_howmany_trucks(P):
    '''
    トラックの数がk、最大積載量がPのとき荷物を載せきれるかを判定する
    '''
    truck = 1
    temp_weight = 0
    for a,b in enumerate(w):
        if b > P:
            return False
        if temp_weight + b > P:
            # print(f"P = {P} truck No {truck} temp_weight {temp_weight+b}")
            truck += 1
            if truck > k:
                return False
            temp_weight = b
        else:
            temp_weight += b

    return True



n,k = input().split()
n = int(n)
k = int(k)

w = [int(input()) for a in range(n)]

min_P = 10000*100000
left = 0
right = min_P
while left != right:
    middle = int((left+right)/2)
    if solve_howmany_trucks(middle):
        right = middle
    else:
        left = middle+1
print(left)

