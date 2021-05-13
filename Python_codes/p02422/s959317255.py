w=raw_input()
n=input()
l=['print','replace','reverse']
for i in range(n):
    c=map(str,raw_input().split())
    if c[0]==l[0]:
        print w[int(c[1]):int(c[2])+1]
    elif c[0]==l[1]:
        w=w[:int(c[1])]+c[3]+w[int(c[2])+1:]
    else:
        w=w[0:int(c[1])]+w[int(c[1]):int(c[2])+1][::-1]+w[int(c[2])+1:]