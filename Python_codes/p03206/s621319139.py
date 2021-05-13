D = int(input())
day = [' Eve' if D==24 else ' Eve Eve' if D==23 else ' Eve Eve Eve' if D==22 else '']
print('Christmas' + day[0])