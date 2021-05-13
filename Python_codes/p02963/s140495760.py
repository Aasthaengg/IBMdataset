'''
　 ∧_,,∧    究極奥義「WAがACになーれ！！」
　（`・ω・)つ━☆・*。
　⊂　　 ノ 　　　・゜+.
　 し’´Ｊ　　*・ 
'''
import sys
input = sys.stdin.readline
n=int(input())
if n==10**18:
    print(0,0,0,10**9,10**9,0)
    exit()
print(0,0,10**9,1,10**9-n%10**9,1+n//10**9)
