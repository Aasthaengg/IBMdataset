def main():
    number = input()
    r_number = number[::-1]

    if int(number) == int(r_number):
        print("Yes")
    else:
        print("No")
main()