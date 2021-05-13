
n=int(input())
#d = [list(map(int,input().split())) for _ in range(s)]

def p(val):
    print(val)

count = 0

#cは1以上で、問題文からN-1 a*b <=N-1のものをもとめる
#aを1からふやしてく、cはaとbが決まれば自動歴に決まるので、
for i in range(1,n):
    count +=(n-1)//i

    

        
p(count)