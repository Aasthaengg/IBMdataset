import sys
n, a, b = [int(i) for i in sys.stdin.readline().split()]
x_ls = [int(i) for i in sys.stdin.readline().split()]
diff_ls = []
for i, x in enumerate(x_ls[:-1]):
    diff_ls.append((x_ls[i+1] - x) * a)
diff_ls = [i if i < b else b for i in diff_ls]
print(sum(diff_ls))