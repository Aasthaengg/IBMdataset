s = input()

#W,Bの総数は変わらない
#WWWWBBBBのような状態になるまでのWの転移回数を求める
wp=s.count('W')

now=0
count=0
for i in range(len(s)):
    if s[i]=='W':
        now+=i
for i in range(wp):
    count+=i
print(now-count)