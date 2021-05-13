N = int(input())
dictionary = dict()
for i in range(N):
    command, string = input().split()
    if command == "insert":
        dictionary[string] = True
    elif dictionary.get(string) == None:
        print("no")
    else:
        print("yes")