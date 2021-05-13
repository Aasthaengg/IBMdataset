import collections
ABC = list(map(str, input().split()))
cnt = collections.Counter(ABC)
 
if cnt[ABC[0]] == 2 or cnt[ABC[1]] == 2 or cnt[ABC[2]] == 2:
    print('Yes')
else:
    print('No')