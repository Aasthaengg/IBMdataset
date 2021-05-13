price = int(input())

change = 0
mod_change = price % 1000
if mod_change != 0:
    change = 1000 - mod_change

print(change)