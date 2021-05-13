func = {
    "+": lambda n: n + 1,
    "-": lambda n: n - 1
}
n = 0
for c in input():
    n = func[c](n)
print(n)