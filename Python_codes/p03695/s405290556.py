n = int(input())
A = tuple(map(int, input().split()))

CO = [0] * 8
o32 = 0
for a in A:
    if a >= 3200:
        o32 += 1
        continue
    for i in range(8):
        if 4*i*100 <= a < 4*(i+1)*100: 
            CO[i] += 1
ans = 0
for count in CO:
    if count > 0:
        ans += 1
print(1 if ans==0 else ans, ans+o32)
