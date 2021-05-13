n = int(input())
fi = [1] * 50
for i in range(2, n + 1):
    fi[i] = fi[i - 1] + fi[i - 2]
print(fi[n])
