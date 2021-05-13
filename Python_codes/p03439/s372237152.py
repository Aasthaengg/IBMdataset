import bisect
def main():
    n = int(input())
    print(0)
    s = input()
    seat_dict = {"Male": 1, "Female": 2}
    if s == "Male":
        ls = [1, 2] * ((n - 1) // 2) + [1] * ((n -1) % 2)
    elif s == "Female":
        ls = [2, 1] * ((n - 1) // 2) + [2] * ((n - 1) % 2)
    else:
        return
    up = n - 1
    down = 0
    for i in range(20):
        mid = (up + down) // 2
        if mid == down:
            mid = up
        print(mid)
        s = input()
        if s == "Vacant":
            break
        _s = seat_dict[s]
        if _s == ls[mid]:
            down = mid
        else:
            up = mid

if __name__ == "__main__":
    main()