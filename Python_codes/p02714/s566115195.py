N = int(input())
S = input()

from collections import defaultdict

memo = [defaultdict(int) for j in range(N+1)]

ans = 0



for i,s in enumerate(S):
    memo[i+1]["R"] = memo[i]["R"]
    memo[i+1]["G"] = memo[i]["G"]
    memo[i+1]["B"] = memo[i]["B"]
    memo[i+1][s]+=1
    others = set(["R","G","B"])
    others.remove(s)
    others = list(others)
    ans += memo[i+1][others[0]] * memo[i+1][others[1]]

rgb = set(["R","G","B"])
# print(rgb)

if N > 2:
    if N %2 == 1:
        length = N // 2
    else:
        length = N // 2 - 1

    # print(length)
    
    for skip in range(length):
        for i in range(len(S)):
            # print(i)
            if i+2+skip*2 > len(S)-1:

                break
            a,b,c = S[i],S[i+1+skip],S[i+2+skip*2]
            # print(set([a,b,c]))
            if set([a,b,c]) == rgb:
                ans -= 1
        

print(ans)
