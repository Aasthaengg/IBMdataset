from collections import defaultdict
n = int(input())

a = list(map(int, input().split()))

dic = defaultdict(int)

ans = 0

# j - aj = ai + iとして、jを固定して考える
# jを一つずつみていって、それまでに出会った物の中からj-ajに等しい物の数を数える。ai + iは記録しておく。
for i in range(len(a)):
    
    t = i - a[i]
    ans += dic[t]
    dic[a[i]+i] += 1

print(ans)
