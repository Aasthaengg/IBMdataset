import math
N = int(input())
ans = ""

for i in range(1, int(math.sqrt(2*N)+1)):
    if i*(i+1) == 2*N:
        k = i
        break
else:
    print("No")
    exit()

for i in range(k+1):
    if i == 0:
        ans += str(k) + " " + " ".join(map(str, range(1, k+1))) + "\n"
        ans_list = [0, k]
    else:
        ans_list = [i+1 for i in ans_list]
        ans += str(k) + " " + " ".join(map(str, ans_list[:-1]+\
        list(range(ans_list[-1], ans_list[-1]+k-i)))) + "\n"
        ans_list = ans_list[:-1] + [ans_list[-1]-1]
        ans_list.append(ans_list[-1]+k-i)


print("Yes"+"\n{}\n".format(k+1)+ans[:-1])