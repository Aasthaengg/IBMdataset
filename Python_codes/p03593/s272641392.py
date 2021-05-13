from string import ascii_lowercase


def new_val(cnt, base, target):
    diff = min(cnt // base, target)
    cnt -= diff * base
    target -= diff
    return cnt, target


def main():
    h, w = map(int, input().split())
    count = {s: 0 for s in ascii_lowercase}
    for _ in range(h):
        row = input()
        for j in range(w):
            count[row[j]] += 1
    target_4 = (h // 2) * (w // 2)
    target_1 = (h % 2) * (w % 2)
    target_2 = (w // 2) * (h % 2) + (h // 2) * (w % 2)
    ans = "Yes"
    for chr, cnt in count.items():
        count[chr], target_4 = new_val(cnt, 4, target_4)
    if target_4:
        ans = "No4"
    for chr, cnt in count.items():
        count[chr], target_2 = new_val(cnt, 2, target_2)
    if target_2:
        ans = "No2"
    if sum(count.values()) != target_1:
        ans = "No"
    print(ans)


if __name__ == '__main__':
    main()

