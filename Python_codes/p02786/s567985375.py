H = int(input())

cnt = 0
def attack(hp, cnt):
    cnt += 1
    if hp == 1:
        return cnt

    cnt += attack(hp//2, 0) * 2
    return cnt

print(attack(H, cnt))
