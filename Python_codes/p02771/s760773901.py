A,B,C = (int(x) for x in input().split())
List = [A,B,C]
if len(set(List))==2:
    print('Yes')
else:
    print('No')