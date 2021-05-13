n = int(input()) 
a_list = list(map(int, input().split()))
res = sorted(range(n), key=lambda k: a_list[k])
print(' '.join(list(map(lambda x: str(x+1), res))))