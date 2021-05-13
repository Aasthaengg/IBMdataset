nn = int(input())
ss = [str(input()) for l in range(nn)]
ss.sort()

keihin = 1
for i in range(nn-1):
    if ss[i] != ss[i+1]:
        keihin += 1

print(keihin)