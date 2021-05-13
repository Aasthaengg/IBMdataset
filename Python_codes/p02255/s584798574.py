def show_list(target):
    for i, item in enumerate(target):
        if i == len(target) - 1:
            print(item)
        else:
            print(item, end=" ")

def insection_sort(target):
    for i in range(1, len(target)):
        show_list(target)
        j = i - 1
        while j >= 0:
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
                j -= 1
            else:
                break
    return target

if __name__ == "__main__":
    n = input()
    a = [int(x) for x in input().split()]
    answer = insection_sort(a)
    show_list(answer)