S = input()
N = int(S)
ans = sum(map(int,S))

for i in range(1,len(S)):
    n = str(int(S[:i]) - 1)
    t = sum(map(int,n)) + 9*(len(S)-i)
    ans = max(ans,t)
print(ans)