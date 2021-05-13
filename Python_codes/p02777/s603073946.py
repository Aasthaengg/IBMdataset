s,t = input().split()
snum, tnum = map(int,input().split())
selection = input()

if (selection == s):
    print(snum-1,tnum)
else:
    print(snum,tnum-1)