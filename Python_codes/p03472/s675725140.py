def main():
    n,h = list(map(int, input().split()))
    bi = []
    max_attack = [0,0]
    for i in range(n):
        a, b = list(map(int, input().split()))
        bi.append(b)
        max_attack[0] = max(a, max_attack[0])
        max_attack[1] = max(b, max_attack[1])
    bi.sort(reverse=True)
    idx = 0
    count = 0
    while h > 0:
        damage = 0
        if idx < len(bi) and max_attack[0] < bi[idx]:
            damage = bi[idx]
            idx += 1
        else:
            count += h // max_attack[0]
            count += 0 if h % max_attack[0] == 0 else 1
            break
        h -= damage
        count += 1
    print(count)



if __name__ == '__main__':
    main()