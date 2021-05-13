def calc():

    amari = N % 500

    if amari <= A:
        return"Yes"

    else:
        return"No"

N = int(input())
A = int(input())

print(calc())