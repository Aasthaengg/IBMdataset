S = list(input())
lst = [chr(i) for i in range(97, 97+26)]
res = sorted(list(set(lst) - set(S)))

if res == []:
    print("None")
else:
    print(res[0])
