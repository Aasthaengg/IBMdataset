n = int(input())
alphabet = list("abcdefghij"[:n])

# DFS
def print_string(string="", depth=1):
    if len(string) == n:
        print(string)
    else:
        for i in range(depth):
            if i+1 == depth:
                print_string(string+alphabet[i], depth=depth+1)
            else:
                print_string(string+alphabet[i], depth=depth)
                
print_string()