def count_up(d, cut):
    ARC = len([1 for i in d if i >= cut])
    ABC = len(d) - ARC
    if ABC == ARC:
        return True
    return False

N = int(input())
d = list(map(int, input().split()))
d.sort()
print(d[N//2] - d[N//2 - 1])