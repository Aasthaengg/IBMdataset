def main():
    number = int(raw_input())
    list = map(int, raw_input().split())
    sort(number, list)

def sort(number, list):
    output(list)
    for i in range(1, number):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
        output(list)

def output(list):
    print(" ".join(map(str, list)))

main()