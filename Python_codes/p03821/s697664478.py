n = int(input()) 
ab = [tuple(map(int,input().split())) for i in range(n)]

push = 0
ab.reverse()

for i in range(len(ab)):
    mod = ( ab[i][0] + push ) % ab[i][1]
    if mod != 0:
        push += ab[i][1] - mod 

print(push)
