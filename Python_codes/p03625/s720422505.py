'''
　 ∧_,,∧    究極奥義「WAがACになーれ！！」
　（`・ω・)つ━☆・*。
　⊂　　 ノ 　　　・゜+.
　 し’´Ｊ　　*・ 
'''
import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
ans=1
cnt=0
i=0
while i<n-1 and cnt<2:
    if a[i]==a[i+1]:
        ans*=a[i]
        i+=2
        cnt+=1
    else:
        i+=1
if cnt==2:
    print(ans)
else:
    print(0)
