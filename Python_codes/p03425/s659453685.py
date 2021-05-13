import itertools
n = int(input())
Dict = {'M':0,'A':1,'R':2,'C':3,'H':4}

List = [[]for i in range(5)]
for i in range(n):
    tmp = input()
    if tmp[0] in Dict:
        index = Dict[tmp[0]]
        List[index].append(tmp)
List_num = [len(List[i]) for i in range(5)]
ans = 0
for v in itertools.combinations(List_num,3):
    cnt = 1
    for youso in v:
        cnt*=youso
    ans += cnt
print(ans)