N = int(input())
S = input()

ans = 0

for i in range(N-1):
    l1 = [0]*26
    l2 = [0]*26
    for j in S[:i+1]:
        if l1[(ord(j)-ord("a"))]==0:
            l1[(ord(j)-ord("a"))]=1
    for k in S[i+1:]:
        if l2[(ord(k)-ord("a"))]==0:
            l2[(ord(k)-ord("a"))]=1
    cnt = 0
    for i in range(26):
        if l1[i]*l2[i] == 1:
            cnt += 1
    ans = max(ans, cnt)

print(ans)