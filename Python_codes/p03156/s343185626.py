N = int(input())
A,B = map(int, input().split())
Ps  = list(map(int, input().split()))

cnt_a = 0
cnt_b = 0
for p in Ps:
    if p <= A:
        cnt_a += 1
    elif p > B:
        cnt_b += 1
print(min(cnt_a,cnt_b,N-cnt_a-cnt_b))
