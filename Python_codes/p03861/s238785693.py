
a, b, x = map(int, input().strip().split())


def func(num1, num2, divide_num):
    ans = num2 // divide_num - (num1 - 1) // divide_num

    print(ans)


func(num1=a, num2=b, divide_num=x)
