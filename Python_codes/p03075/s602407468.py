x = [int(input()) for i in range(5)]
y = int(input())
if max(x)-min(x) <= y:
    print("Yay!")
else:
    print(":(")
