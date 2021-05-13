N = int(input())

for i in range(10):
    if 111*i < N <= 111*(i+1):
        print(111*(i+1))