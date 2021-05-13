# APC001C - Vacant Seat
def main():
    # if no vacant seat in [0, i)
    # -> seat[0] == seat[i] if i % 2 else seat[0] != seat[i]
    N = int(input())
    print(0, flush=1)
    seat_zero = input().rstrip()
    if seat_zero == "Vacant":
        return
    left, right = 0, N
    for _ in range(19):
        mid = (left + right) // 2
        print(mid, flush=1)
        this_seat = input().rstrip()
        if this_seat == "Vacant":
            return
        if mid % 2 == (seat_zero != this_seat):
            left = mid
        else:
            right = mid


if __name__ == "__main__":
    main()