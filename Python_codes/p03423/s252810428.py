a = int(input())
def more_than_three(a):
    if a < 3:
        return 0
    else:
        return a//3
print(more_than_three(a))