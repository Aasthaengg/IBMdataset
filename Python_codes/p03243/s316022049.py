n = int(input())
a = [str(i+1)*3 for i in range(9)]
for i in a:
    if n<=int(i):
        print(int(i))
        break