import sys
my_str = input()

for i in range(len(my_str)):
    if "a" <= my_str[i] <= "z":
        sys.stdout.write(my_str[i].upper())
    elif "A" <= my_str[i] <= "Z":
        sys.stdout.write(my_str[i].lower())
    else:
        sys.stdout.write(my_str[i])
sys.stdout.write("\n")