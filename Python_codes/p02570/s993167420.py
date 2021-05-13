def ap_in_time(distance, time_for_ap, speed) -> str:
    return 'Yes' if distance <= time_for_ap * speed else 'No'


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(ap_in_time(a, b, c))