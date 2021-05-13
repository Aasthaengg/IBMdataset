n = int(input())
list = [int(input()) for _ in range(n)]

def main(n, list):
    result = 0
    num = 0
    if list[0] != 0:
        return -1
    
    for i in range(n - 1, - 1, - 1):
        if list[i] >= num:
            result += list[i]
            num = list[i]
        elif list[i] == num - 1:
            num -= 1
        else:
            return -1
    return result

print(main(n, list))