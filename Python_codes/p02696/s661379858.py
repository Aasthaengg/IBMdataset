import sys
a, b, n = map(int, input().split())

if n < b:
    ans = a * n // b  
    print(ans)
    sys.exit()  
elif n == b:
    ans = a * (b-1) // b
    print(ans)
    sys.exit()

# n == 1のときは0 問題なし
r = n // b
ans = 0
# for i in range(1, r + 1):
#     t = i * b - 1
#     ans_t = a * t // b - (a * (i - 1))
#     ans = max(ans, ans_t) 
    # print(i, t, ans)

t = r * b - 1
ans_t = a * t // b - (a * (r - 1))
ans = max(ans, ans_t) 

ans_t = a * n // b - (a * (n // b))
ans = max(ans, ans_t) 

print(ans)