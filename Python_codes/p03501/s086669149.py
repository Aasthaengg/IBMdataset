def main():
    parking_hour, fee_par_hour, flat_fee = map(int, input().split())
    print(min(parking_hour * fee_par_hour, flat_fee))


if __name__ == '__main__':
    main()