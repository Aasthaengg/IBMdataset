# ABC85 D 
import math

def main():
    N, H = list(map(int, input().split()))
    a_max = 0
    b_list = []

    for _ in range(N):
        a,b = list(map(int, input().split()))
        a_max = max(a, a_max)
        b_list.append(b)

    b_list = sorted(b_list)[::-1]
    
    cnt = 0
    for b in b_list:
        if b < a_max:
            break
        if H <= 0:
            break
        H -= b
        cnt += 1
    
    if H > 0:
        print(cnt + math.ceil(H / a_max))
    else:
        print(cnt)

if __name__ == "__main__":
    main()
