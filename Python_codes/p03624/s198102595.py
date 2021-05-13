S = sorted(list(input()))

if len(set(S)) == 26:
    print("None")
    exit()

S = sorted(list(set(S)))

s = list("abcdefghijklmnopqrstuvwxyz")

def list_difference(list1, list2):
    result = list1.copy()
    for value in list2:
        if value in result:
            result.remove(value)

    return result

result = list_difference(s,S)

print(result[0])