a,b = input().split(" ")
lst = list(map(int,input().split(" ")))
lst_s = sorted(lst)
res = lst_s[0:int(b)]
print(sum(res))