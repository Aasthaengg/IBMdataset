n = int(input())
dic1 = {}
for i in range(n):
    s = input()
    if s not in dic1.keys():
        dic1[s] = 1
    else:
        dic1[s] += 1
dic2 = sorted(dic1.items(), key=lambda j: j[1], reverse=True)

ans_ls = []
for k in range(len(dic2)):
    if dic2[k][1] != dic2[0][1]:
        break
    ans_ls.append(dic2[k][0])
ans_ls.sort()
for _ in ans_ls:
  	print(_)