input()
*l,=map(int,input().split())
print( len(set([1 for i in l if i%2==0 and (i%3!=0 and i%5!=0)]))*"DENIED" or 'APPROVED') 